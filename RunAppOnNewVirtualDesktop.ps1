#https://superuser.com/questions/995236/how-to-create-new-virtual-desktops-in-a-script-to-launch-multiple-applications-i
$KeyShortcut = Add-Type -MemberDefinition @"
[DllImport("user32.dll")]
static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, UIntPtr dwExtraInfo);

//WIN + CTRL + D: Create a new desktop
public static void CreateVirtualDesktopInWin10()
{
    //Key down
    keybd_event((byte)0x5B, 0, 0, UIntPtr.Zero); //Left Windows key 
    keybd_event((byte)0x11, 0, 0, UIntPtr.Zero); //CTRL
    keybd_event((byte)0x44, 0, 0, UIntPtr.Zero); //D
    //Key up
    keybd_event((byte)0x5B, 0, (uint)0x2, UIntPtr.Zero);
    keybd_event((byte)0x11, 0, (uint)0x2, UIntPtr.Zero);
    keybd_event((byte)0x44, 0, (uint)0x2, UIntPtr.Zero);
}

//WIN + CTRL + LEFT ARROW: switch to the left
public static void Switch2PreviousVirtualDesktop()
{
    //Key down
    keybd_event((byte)0x5B, 0, 0, UIntPtr.Zero); //Left Windows key 
    keybd_event((byte)0x11, 0, 0, UIntPtr.Zero); //CTRL
    keybd_event((byte)0x25, 0, 0, UIntPtr.Zero); //D
    //Key up
    keybd_event((byte)0x5B, 0, (uint)0x2, UIntPtr.Zero);
    keybd_event((byte)0x11, 0, (uint)0x2, UIntPtr.Zero);
    keybd_event((byte)0x25, 0, (uint)0x2, UIntPtr.Zero);
}



"@ -Name CreateVirtualDesktop -UsingNamespace System.Threading -PassThru

$KeyShortcut::CreateVirtualDesktopInWin10()
calc
Start-Sleep -m 500
for (($i = 0), ($j = 0); $i -lt 20; $i++)
{
	$KeyShortcut::Switch2PreviousVirtualDesktop()
}
