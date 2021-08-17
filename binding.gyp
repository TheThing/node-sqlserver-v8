{
  'targets': [
    {
      'target_name': 'sqlserverv8',

      'variables': {
        'conditions': [
            [
              'OS=="mac"', {
                    'arch%': [
                      '<!(uname -m)',
                    ]
              },
              'OS=="linux"', {
                    'arch%': [
                      '<!(uname -m)',
                    ]
              },
              'OS=="win"', {
                  'arch%': [
                    '<!(echo %PROCESSOR_ARCHITECTURE%)'
                ]
              }
            ]
        ],
        'target%': '<!(node -e "console.log(process.versions.node)")', # Set the target variable only if it is not passed in by prebuild 
      },

      'sources': [
        'src/ConnectionHandles.cpp',
        'src/bcp.cpp',
        'src/addon.cpp',
        'src/QueryOperationParams.cpp',
        'src/MutateJS.cpp',
        'src/BoundDatum.cpp',
        'src/BoundDatumSet.cpp',
        'src/ResultSet.cpp',
        'src/Column.cpp',
        'src/BinaryColumn.cpp',
        'src/TimestampColumn.cpp',
        'src/OdbcConnection.cpp',
        'src/CollectOperation.cpp',
        'src/EndTranOperation.cpp',
        'src/CancelOperation.cpp',
        'src/OpenOperation.cpp',
        'src/PrepareOperation.cpp',
        'src/PollingModeOperation.cpp',
        'src/ProcedureOperation.cpp',
        'src/QueryOperation.cpp',
        'src/ReadColumnOperation.cpp',
        'src/QueryPreparedOperation.cpp',
        'src/FreeStatementOperation.cpp',
        'src/ReadNextResultOperation.cpp',
        'src/OdbcStatement.cpp',
        'src/BeginTranOperation.cpp',
        'src/CloseOperation.cpp',
        'src/OdbcOperation.cpp',
        'src/OdbcHandle.cpp',        
        'src/UnbindOperation.cpp',
        'src/OdbcStatementCache.cpp',
        'src/OdbcError.cpp',
        'src/OdbcConnectionBridge.cpp',
        'src/Operation.cpp',
        'src/OperationManager.cpp',
        'src/Utility.cpp', 
        'src/Connection.cpp',
        'src/stdafx.cpp'
		  ],

      'include_dirs': [
        "<!(node -e \"require('nan')\")",
        'src',
      ],

     'defines': [ 'NODE_GYP_V4' ],

      'conditions': [
        ['target < "13.0"', {
                  'defines': [
                    'PRE_V13',
                  ],
           },
           'arch == "arm64"',{
             'LINK_LIB%': ['/opt/homebrew/lib/libodbc.a']
           },
           'arch == "x86_64"',{
             'LINK_LIB%': ['-lodbc']
           },
        ],
        [ 'OS=="win"', {
              'link_settings': {
             'libraries': [
               'odbc32'
               ],
            },
          'defines': [
            'UNICODE=1',
            'WINDOWS_BUILD',
          ],
          }
        ],
        ['OS=="linux"', {
            'link_settings': {
             'libraries': [
               '-lodbc',
               ],
            },
            'defines': [
              'LINUX_BUILD',
              'UNICODE'
            ], 
            'cflags_cc': [
              '-std=c++1y'
            ],
            'include_dirs': [
              '/usr/include/',
              '/opt/microsoft/msodbcsql17/include/',
            ],
        }],
        ['OS=="mac"', {
            'link_settings': {
             'libraries': ['<!@(LINK_LIB)'],
            },
            'defines': [
              'LINUX_BUILD',
              'UNICODE'
            ], 
            'cflags_cc': [
              '-std=c++1y'
            ],
            'include_dirs': [
              '/opt/homebrew/include',
              '/opt/homebrew/include/msodbcsql17'
              '/usr/local/include/',
              '/usr/local/opt/msodbcsql17/include/',
              '/usr/local/opt/msodbcsql17/include/msodbcsql17/'
            ],
        }],
      ]
    }
  ]
}
