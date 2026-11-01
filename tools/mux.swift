// Put an AAC audio track under an H.264 video without re-encoding either.
//   swiftc -O -o tools/.mux tools/mux.swift
//   tools/.mux <video.mp4> <audio.m4a> <out.mp4>
import AVFoundation
import Foundation

let a = CommandLine.arguments
guard a.count == 4 else {
    print("usage: mux <video> <audio> <out>")
    exit(2)
}
let video = AVURLAsset(url: URL(fileURLWithPath: a[1]))
let audio = AVURLAsset(url: URL(fileURLWithPath: a[2]))
let comp = AVMutableComposition()
guard let vTrack = video.tracks(withMediaType: .video).first,
      let aTrack = audio.tracks(withMediaType: .audio).first,
      let cv = comp.addMutableTrack(withMediaType: .video, preferredTrackID: kCMPersistentTrackID_Invalid),
      let ca = comp.addMutableTrack(withMediaType: .audio, preferredTrackID: kCMPersistentTrackID_Invalid) else {
    print("missing a track")
    exit(1)
}
let range = CMTimeRange(start: .zero, duration: video.duration)
try cv.insertTimeRange(range, of: vTrack, at: .zero)
let audioRange = CMTimeRange(start: .zero, duration: CMTimeMinimum(audio.duration, video.duration))
try ca.insertTimeRange(audioRange, of: aTrack, at: .zero)
let out = URL(fileURLWithPath: a[3])
try? FileManager.default.removeItem(at: out)
guard let export = AVAssetExportSession(asset: comp, presetName: AVAssetExportPresetPassthrough) else {
    print("no export session")
    exit(1)
}
export.outputURL = out
export.outputFileType = .mp4
let done = DispatchSemaphore(value: 0)
export.exportAsynchronously { done.signal() }
done.wait()
if export.status != .completed {
    print("export failed: \(export.error?.localizedDescription ?? "unknown")")
    exit(1)
}
