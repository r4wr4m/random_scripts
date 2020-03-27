echo "Suspending VMs..."
IFS=$'\n'
for i in $(vmrun list | grep .vmx)
do
echo "[*] Suspending $i"
x="${i// /\\ }"
echo "$x"
vmrun suspend $x
done
echo "[*] Nothing left to suspend."
echo "NARA"
shutdown now
