mkdir -p /ram
if ! mountpoint -q -- "/ram"; then
  mount -t tmpfs -o size=50M tmpfs /ram
  printf "created a ramdisk at /ram\n"
fi