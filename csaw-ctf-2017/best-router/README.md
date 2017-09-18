# Challenge

http://forensics.chal.csaw.io:3287

NOTE: This will expand to ~16GB!

# Walkthrough/Solution

Unzipping the file gives us `best_router.img`. Running the `fdisk -l` command on it shows us the necessary information for us to work with this image:

```
#fdisk -l best_router.img

Disk best_router.img: 14.6 GiB, 15640559616 bytes, 30547968 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x7f39f284

Device           Boot Start      End  Sectors  Size Id Type
best_router.img1       8192    93813    85622 41.8M  c W95 FAT32 (LBA)
best_router.img2      94208 30547967 30453760 14.5G 83 Linux
```
I mounted this image by using the following command below. Note that the offset is calculated by multiplying the sector size and the start sector of the filesystem.
```
#mount -o loop,offset=48234496 best_router.img /mount
```
Navigating to the root folder through `cd ./root`, I found a file `install.sh`.
```
install.sh

sudo apt-get update
sudo apt-get install apache2 -y
sudo a2enmod cgid

sudo cp 000-default.conf /etc/apache2/sites-available/000-default.conf
sudo service apache2 restart

sudo rm -rf /var/www/*
sudo mv www/* /var/www
chmod 755 /var/www/*.pl
```
Navigating to the `/var/www` folder shows us `username.txt` and `password.txt`. These are the credentials to the website at `http://forensics.chal.csaw.io:3287/`.

Logging in with the credentials gives us the flag `flag{but_I_f0rgot_my_my_math_test_and_pants}`.

# Learning outcome
1. Mounting .img files
2. Identifying patterns
