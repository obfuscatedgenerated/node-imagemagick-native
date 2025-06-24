import winreg

def get_regvalue(regkey, regvalue):

    explorer = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        regkey,
        0,
        winreg.KEY_READ | winreg.KEY_WOW64_64KEY
    )
    
    value, type = winreg.QueryValueEx(explorer, regvalue)

    return value

print(get_regvalue('SOFTWARE\\ImageMagick\\Current', 'LibPath'))
