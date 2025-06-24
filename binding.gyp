{
  'conditions': [
    ['OS=="win"', {
      'variables': {
        'MAGICK_ROOT%': '<!(python get_regvalue.py)',
        'OSX_VER%': "0",
      }
    }],
    ['OS=="mac"', {
      'variables': {
        'OSX_VER%': "<!(sw_vers | grep 'ProductVersion:' | grep -o '10.[0-9]*')",
      }
    }, {
      'variables': {
        'OSX_VER%': "0",
      }
    }]
  ],
  "targets": [
    {
      "target_name": "imagemagick",
      "sources": [ "src/imagemagick.cc" ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'cflags': [ '-v' ],
      'cflags_cc': [ '-v' ],
      'ldflags': [ '-Wl,-v' ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        ['OS=="win"', {
          "libraries": [
            '-l<(MAGICK_ROOT)/lib/CORE_RL_magick_.lib',
            '-l<(MAGICK_ROOT)/lib/CORE_RL_Magick++_.lib',
            '-l<(MAGICK_ROOT)/lib/CORE_RL_wand_.lib',
          ],
          'include_dirs': [
            '<(MAGICK_ROOT)/include',
          ],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'AdditionalOptions': ['/verbose'],
            },
            'VCLinkerTool': {
              'AdditionalOptions': ['/VERBOSE'],
            }
          }
        }],
        ['OS=="win" and target_arch!="x64"', {
          'defines': [
            '_SSIZE_T_',
          ]
        }],
        ['OSX_VER == "10.9" or OSX_VER == "10.10" or OSX_VER == "10.11" or OSX_VER == "10.12" or OSX_VER == "10.13"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
              '<!@(pkg-config --cflags ImageMagick++)',
              '-v'
            ],
            'OTHER_CPLUSPLUSFLAGS' : [
              '<!@(pkg-config --cflags ImageMagick++)',
              '-std=c++11',
              '-stdlib=libc++',
              '-v'
            ],
            'OTHER_LDFLAGS': [
              '-stdlib=libc++',
              '-Wl,-v'
            ],
            'MACOSX_DEPLOYMENT_TARGET': '10.7',
          },
          "libraries": [
             '<!@(pkg-config --libs ImageMagick++)',
          ],
          'cflags': [
            '<!@(pkg-config --cflags ImageMagick++)',
            '-v'
          ],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
              '<!@(pkg-config --cflags ImageMagick++)',
              '-v'
            ],
            'OTHER_LDFLAGS': [ '-Wl,-v' ]
          },
          "libraries": [
             '<!@(pkg-config --libs ImageMagick++)',
          ],
          'cflags': [
            '<!@(pkg-config --cflags ImageMagick++)',
            '-v'
          ],
        }],
        ['OS=="linux" or OS=="solaris" or OS=="freebsd"', {
          "libraries": [
            '<!@(pkg-config --libs ImageMagick++)',
          ],
          'cflags': [
            '<!@(pkg-config --cflags ImageMagick++)',
            '-v'
          ],
          'ldflags': [ '-Wl,-v' ]
        }]
      ]
    }
  ]
}
