# THunarCA
this is just a simple custom action that are useful with thunar 



#Sharing Files 

### http sharing -linux : 
  ```
     echo "wget 'http://ip/$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ; x-terminal-emulator -e "python3 -m http.server 80"
  ```
### http sharing -windows cmd : 
  ```

 echo  "certutil -urlcache -f 'http://ip/$(echo %N | sed "s/'//g")' '$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ; x-terminal-emulator -e "python3 -m http.server 80"
```
### http sharing -windows powershell : 
  ```


  echo "Invoke-WebRequest -Uri 'http://ip/$(echo %N | sed "s/'//g")' -OutFile '$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ;  -e "python3 -m http.server 80"
```

### smb sharing -windows : 
```
echo "copy '\\\\ip\\share\\$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ; x-terminal-emulator -e "sudo impacket-smbserver share -smb2support '%d'"
```

### smb sharing -windows -password 
```
echo "net use n: \\\\ip\\\share /user:wiwsmb wiwsmb" | xclip -selection clipboard ; x-terminal-emulator -e "sudo impacket-smbserver share -smb2support '%d' -user wiwsmb -password wiwsmb"
```

### SSH sharing 

