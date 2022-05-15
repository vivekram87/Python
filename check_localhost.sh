if grep "127.0.0.1" /etc/hosts; then 
	    echo “Everything is OK”
else
  	    echo “Error 127.0.0.1 not in /etc/hosts”
fi
