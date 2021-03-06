# Copyright (c) 2012 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.
{
  'targets': [
    {
      'target_name': 'video_demo_apk',
      'type': 'none',
      'dependencies': [
        '<(webrtc_root)/modules/modules.gyp:*',
        '<(webrtc_root)/test/test.gyp:channel_transport',
        '<(webrtc_root)/video_engine/video_engine.gyp:video_engine_core',
        '<(webrtc_root)/voice_engine/voice_engine.gyp:voice_engine',
      ],
      'actions': [
        {
          # TODO(leozwang): Convert building of the demo to a proper GYP target
          # so this action and the custom build script is not needed.
          # (http://crbug.com/255101)
          'action_name': 'build_video_demo_apk',
          'inputs' : [
            '<(webrtc_root)/video_engine/test/android/src/org/webrtc/videoengine/ViEMediaCodecDecoder.java',
            '<(webrtc_root)/video_engine/test/android/src/org/webrtc/videoengineapp/IViEAndroidCallback.java',
            '<(webrtc_root)/video_engine/test/android/src/org/webrtc/videoengineapp/ViEAndroidJavaAPI.java',
            '<(webrtc_root)/video_engine/test/android/src/org/webrtc/videoengineapp/WebRTCDemo.java',
          ],
          'outputs': ['<(webrtc_root)'],
          'action': ['python',
                     '<(webrtc_root)/video_engine/test/android/build_demo.py',
                     '--arch', '<(target_arch)'],
        },
      ],
    },
  ],
}

