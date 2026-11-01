// Cut a stretch of a video into 1080x1920 JPEG frames at 30 fps, filling the frame (centre crop).
// render.py lays the words over these, the same way it does over a Blender scene.
//   swiftc -O -o tools/.clip-frames tools/clip-frames.swift
//   tools/.clip-frames <in.mp4> <start seconds> <duration seconds> <out dir> <first index>
import AVFoundation
import CoreImage
import Foundation
import ImageIO
import UniformTypeIdentifiers

let a = CommandLine.arguments
guard a.count == 6, let start = Double(a[2]), let duration = Double(a[3]), let first = Int(a[5]) else {
    print("usage: clip-frames <in> <start> <duration> <out dir> <first index>")
    exit(2)
}
let W = 1080.0, H = 1920.0, FPS = 30.0
let asset = AVURLAsset(url: URL(fileURLWithPath: a[1]))
let gen = AVAssetImageGenerator(asset: asset)
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = CMTime(value: 1, timescale: 120)
gen.requestedTimeToleranceAfter = CMTime(value: 1, timescale: 120)
let ctx = CIContext()
let outDir = URL(fileURLWithPath: a[4])
let total = Int((duration * FPS).rounded())
let clipLength = CMTimeGetSeconds(asset.duration)
for i in 0..<total {
    // A clip shorter than the stretch asked for plays to its end and holds; it never loops.
    let t = min(start + Double(i) / FPS, max(0, clipLength - 0.05))
    guard let cg = try? gen.copyCGImage(at: CMTime(seconds: t, preferredTimescale: 600), actualTime: nil) else { continue }
    var img = CIImage(cgImage: cg)
    let scale = max(W / img.extent.width, H / img.extent.height)
    img = img.transformed(by: CGAffineTransform(scaleX: scale, y: scale))
    let x = (img.extent.width - W) / 2, y = (img.extent.height - H) / 2
    img = img.cropped(to: CGRect(x: img.extent.minX + x, y: img.extent.minY + y, width: W, height: H))
        .transformed(by: CGAffineTransform(translationX: -(img.extent.minX + x), y: -(img.extent.minY + y)))
    guard let out = ctx.createCGImage(img, from: CGRect(x: 0, y: 0, width: W, height: H)) else { continue }
    let url = outDir.appendingPathComponent(String(format: "%05d.jpg", first + i))
    guard let dest = CGImageDestinationCreateWithURL(url as CFURL, UTType.jpeg.identifier as CFString, 1, nil) else { continue }
    CGImageDestinationAddImage(dest, out, [kCGImageDestinationLossyCompressionQuality: 0.92] as CFDictionary)
    CGImageDestinationFinalize(dest)
}
