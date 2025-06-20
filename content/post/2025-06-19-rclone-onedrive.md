---
layout: post
title: 'rclone建立远程连接'
date: 2025-06-19 23:25:55
categories: [linux]
tags: [linux]
draft: false
excerpt_separator: <!--more-->
---
rclone建立远程连接
<!--more-->

## 建立远程连接

```bash
rclone config

No remotes found, make a new one?
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n

Enter name for new remote.
name> drive

Option Storage.
Type of storage to configure.
Choose a number from below, or type in your own value.
 1 / 1Fichier
   \ (fichier)
 2 / Akamai NetStorage
   \ (netstorage)
 3 / Alias for an existing remote
   \ (alias)
 4 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, ArvanCloud, Ceph, ChinaMobile, Cloudflare, DigitalOcean, Dreamhost, GCS, HuaweiOBS, IBMCOS, IDrive, IONOS, LyveCloud, Leviia, Liara, Linode, Magalu, Minio, Netease, Petabox, RackCorp, Rclone, Scaleway, SeaweedFS, StackPath, Storj, Synology, TencentCOS, Wasabi, Qiniu and others
   \ (s3)
 5 / Backblaze B2
   \ (b2)
 6 / Better checksums for other remotes
   \ (hasher)
 7 / Box
   \ (box)
 8 / Cache a remote
   \ (cache)
 9 / Citrix Sharefile
   \ (sharefile)
10 / Combine several remotes into one
   \ (combine)
11 / Compress a remote
   \ (compress)
12 / Dropbox
   \ (dropbox)
13 / Encrypt/Decrypt a remote
   \ (crypt)
14 / Enterprise File Fabric
   \ (filefabric)
15 / FTP
   \ (ftp)
16 / Files.com
   \ (filescom)
17 / Gofile
   \ (gofile)
18 / Google Cloud Storage (this is not Google Drive)
   \ (google cloud storage)
19 / Google Drive
   \ (drive)
20 / Google Photos
   \ (google photos)
21 / HTTP
   \ (http)
22 / Hadoop distributed file system
   \ (hdfs)
23 / HiDrive
   \ (hidrive)
24 / ImageKit.io
   \ (imagekit)
25 / In memory object storage system.
   \ (memory)
26 / Internet Archive
   \ (internetarchive)
27 / Jottacloud
   \ (jottacloud)
28 / Koofr, Digi Storage and other Koofr-compatible storage providers
   \ (koofr)
29 / Linkbox
   \ (linkbox)
30 / Local Disk
   \ (local)
31 / Mail.ru Cloud
   \ (mailru)
32 / Mega
   \ (mega)
33 / Microsoft Azure Blob Storage
   \ (azureblob)
34 / Microsoft Azure Files
   \ (azurefiles)
35 / Microsoft OneDrive
   \ (onedrive)
36 / OpenDrive
   \ (opendrive)
37 / OpenStack Swift (Rackspace Cloud Files, Blomp Cloud Storage, Memset Memstore, OVH)
   \ (swift)
38 / Oracle Cloud Infrastructure Object Storage
   \ (oracleobjectstorage)
39 / Pcloud
   \ (pcloud)
40 / PikPak
   \ (pikpak)
41 / Pixeldrain Filesystem
   \ (pixeldrain)
42 / Proton Drive
   \ (protondrive)
43 / Put.io
   \ (putio)
44 / QingCloud Object Storage
   \ (qingstor)
45 / Quatrix by Maytech
   \ (quatrix)
46 / SMB / CIFS
   \ (smb)
47 / SSH/SFTP
   \ (sftp)
48 / Sia Decentralized Cloud
   \ (sia)
49 / Storj Decentralized Cloud Storage
   \ (storj)
50 / Sugarsync
   \ (sugarsync)
51 / Transparently chunk/split large files
   \ (chunker)
52 / Uloz.to
   \ (ulozto)
53 / Union merges the contents of several upstream fs
   \ (union)
54 / Uptobox
   \ (uptobox)
55 / WebDAV
   \ (webdav)
56 / Yandex Disk
   \ (yandex)
57 / Zoho
   \ (zoho)
58 / premiumize.me
   \ (premiumizeme)
59 / seafile
   \ (seafile)
Storage> 35

Option client_id.
OAuth Client Id.
Leave blank normally.
Enter a value. Press Enter to leave empty.
client_id>

Option client_secret.
OAuth Client Secret.
Leave blank normally.
Enter a value. Press Enter to leave empty.
client_secret>

Option region.
Choose national cloud region for OneDrive.
Choose a number from below, or type in your own value of type string.
Press Enter for the default (global).
 1 / Microsoft Cloud Global
   \ (global)
 2 / Microsoft Cloud for US Government
   \ (us)
 3 / Microsoft Cloud Germany
   \ (de)
 4 / Azure and Office 365 operated by Vnet Group in China
   \ (cn)
region> 1

Edit advanced config?
y) Yes
n) No (default)
y/n> n

Use web browser to automatically authenticate rclone with remote?
 * Say Y if the machine running rclone has a web browser you can use
 * Say N if running rclone on a (remote) machine without web browser access
If not sure try Y. If Y failed, try N.

y) Yes (default)
n) No
y/n> n

Option config_token.
For this to work, you will need rclone available on a machine that has
a web browser available.
For more help and alternate methods see: https://rclone.org/remote_setup/
Execute the following on the machine with the web browser (same rclone
version recommended):
        rclone authorize "onedrive"
Then paste the result.
Enter a value.
#输入产生的token

Option config_type.
Type of connection
Choose a number from below, or type in an existing value of type string.
Press Enter for the default (onedrive).
 1 / OneDrive Personal or Business
   \ (onedrive)
 2 / Root Sharepoint site
   \ (sharepoint)
   / Sharepoint site name or URL
 3 | E.g. mysite or https://contoso.sharepoint.com/sites/mysite
   \ (url)
 4 / Search for a Sharepoint site
   \ (search)
 5 / Type in driveID (advanced)
   \ (driveid)
 6 / Type in SiteID (advanced)
   \ (siteid)
   / Sharepoint server-relative path (advanced)
 7 | E.g. /teams/hr
   \ (path)
config_type> 1

Option config_driveid.
Select drive you want to use
Choose a number from below, or type in your own value of type string.
Press Enter for the default

config_driveid> 4

Drive OK?

Found drive "root" of type "personal"
URL: https://onedrive.live.com?xxxx

y) Yes (default)
n) No
y/n> y

Configuration complete.

Keep this "drive" remote?
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y

Current remotes:

Name                 Type
====                 ====
drive             onedrive

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q
```