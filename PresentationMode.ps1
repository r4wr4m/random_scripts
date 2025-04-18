#https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate
#https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/add-type?view=powershell-7.5
################### powershell
Add-Type -memberDefinition '[DllImport("kernel32.dll")] public static extern void SetThreadExecutionState(uint flags);' -Name screenholder -Namespace Win32 
[Win32.screenholder]::SetThreadExecutionState(2147483651)   
################### powershell
Add-Type -memberDefinition '[DllImport("kernel32.dll")] public static extern void SetThreadExecutionState(uint flags);' -Name screenholder -Namespace Win32;[Win32.screenholder]::SetThreadExecutionState(2147483651);cls;Write-Host 'SCREENHOLDER';Write-Host 'Press any key to exit...';$k =[System.Console]::ReadKey()
################### cmd
powershell -command "Add-Type -memberDefinition '[DllImport(\"kernel32.dll\")] public static extern void SetThreadExecutionState(uint flags);' -Name screenholder -Namespace Win32;[Win32.screenholder]::SetThreadExecutionState(2147483651);cls;Write-Host 'SCREENHOLDER';Write-Host 'Press any key to exit...';$k =[System.Console]::ReadKey()"
################### cmd
powershell -enc QQBkAGQALQBUAHkAcABlACAALQBtAGUAbQBiAGUAcgBEAGUAZgBpAG4AaQB0AGkAbwBuACAAJwBbAEQAbABsAEkAbQBwAG8AcgB0ACgAIgBrAGUAcgBuAGUAbAAzADIALgBkAGwAbAAiACkAXQAgAHAAdQBiAGwAaQBjACAAcwB0AGEAdABpAGMAIABlAHgAdABlAHIAbgAgAHYAbwBpAGQAIABTAGUAdABUAGgAcgBlAGEAZABFAHgAZQBjAHUAdABpAG8AbgBTAHQAYQB0AGUAKAB1AGkAbgB0ACAAZgBsAGEAZwBzACkAOwAnACAALQBOAGEAbQBlACAAcwBjAHIAZQBlAG4AaABvAGwAZABlAHIAIAAtAE4AYQBtAGUAcwBwAGEAYwBlACAAVwBpAG4AMwAyADsAWwBXAGkAbgAzADIALgBzAGMAcgBlAGUAbgBoAG8AbABkAGUAcgBdADoAOgBTAGUAdABUAGgAcgBlAGEAZABFAHgAZQBjAHUAdABpAG8AbgBTAHQAYQB0AGUAKAAyADEANAA3ADQAOAAzADYANQAxACkAOwBjAGwAcwA7AFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAnAFMAQwBSAEUARQBOAEgATwBMAEQARQBSACcAOwBXAHIAaQB0AGUALQBIAG8AcwB0ACAAJwBQAHIAZQBzAHMAIABhAG4AeQAgAGsAZQB5ACAAdABvACAAZQB4AGkAdAAuAC4ALgAnADsAJABrACAAPQBbAFMAeQBzAHQAZQBtAC4AQwBvAG4AcwBvAGwAZQBdADoAOgBSAGUAYQBkAEsAZQB5ACgAKQA=
###################
#powercfg.exe /requests
