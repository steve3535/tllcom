### Problem with ElasticSerach   
* A service with web frontend having a search bar backed by elastic
* the search is throwing an error
* the error is caused by elastic service that keeps crashing
* even if restarted, it will crash again
* check the elastic logs for OOM
* problem is with the Java heap size of elastic
* interrogate in CLI the api of elastic to check current heap size utilization
* change the heap space size in the JVM options of elastic  
* monitor the stability  
* set up a prometheurs exporter for this purpose and observe the behavior in grafana

### Leak memory issue  
* A memory leak issue due to a goferd client trying to connect to amqps in Satellite/Foreman  

### HTTPD 403 
* bad context on the index file under /var/ww/html  
* `curl -I -s -o /dev/null -w '%{http_code}'`  
* instead of semanage fcontext, just restorecon -R -v

### SSH Connection authorized but closed  
* the user has /bin/false or /sbin/nologin as shell  
* chssh vs usermod -s
* lastlog command

  
