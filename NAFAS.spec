# -*- mode: python -*-

block_cipher = None

nafas_version = "1.4"

a = Analysis(['nafas/__main__.py'],
             pathex=['nafas'],
             binaries=[],
             datas=[('nafas/sounds/silence.wav', 'nafas/sounds'), ('nafas/sounds/us1/*.wav', 'nafas/sounds/us1')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='NAFAS-'+nafas_version,
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
		  icon='otherfiles/icon.ico',
		  version="otherfiles/Version.rc",
          console=True )
