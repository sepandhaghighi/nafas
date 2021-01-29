# -*- mode: python -*-

block_cipher = None


a = Analysis(['nafas/__main__.py'],
             pathex=['nafas'],
             binaries=[],
             datas=[('nafas/sounds/*.wav', 'nafas/sounds')],
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
          name='NAFAS',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
		  icon='otherfiles/icon.ico',
		  version="otherfiles/Version.rc",
          console=True )
