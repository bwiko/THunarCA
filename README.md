# THunarCA
this is just a simple custom action that are useful with thunar 



#Sharing Files 

### http sharing -linux : 
  ```
     echo "wget 'http://$(vselector ip)/$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ; x-terminal-emulator -e "python3 -m http.server 80"
  ```
### http sharing -windows cmd : 
  ```

 echo  "certutil -urlcache -f 'http://$(vselector ip)/$(echo %N | sed "s/'//g")' '$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ; x-terminal-emulator -e "python3 -m http.server 80"
```
### http sharing -windows powershell : 
  ```


  echo "Invoke-WebRequest -Uri 'http://$(vselector ip)/$(echo %N | sed "s/'//g")' -OutFile '$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ;  -e "python3 -m http.server 80"
```

### smb sharing -windows : 
```
echo "copy '\\\\$(vselector ip)\\share\\$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ; x-terminal-emulator -e "sudo impacket-smbserver share -smb2support '%d'"
```

### smb sharing -windows -password 
```
echo "net use n: \\\\$(vselector ip)\\\share /user:wiwsmb wiwsmb && copy 'n:\\$(echo %N | sed "s/'//g")'" | xclip -selection clipboard ; x-terminal-emulator -e "sudo impacket-smbserver share -smb2support '%d' -user wiwsmb -password wiwsmb"
```

### SSH sharing 
```
echo "scp  %f $(vselector victim)@$(vselector target):/tmp/" |  xclip -selection clipboard
```
**Note : if you want to integrate variable into your custom action use [vselector script](https://github.com/bwiko/THunarCA/tree/main/scripts) just add the variable into the json file and put it under `/bin/`**
