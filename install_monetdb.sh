echo "deb https://dev.monetdb.org/downloads/deb/ $(lsb_release -cs) monetdb" >> /etc/apt/sources.list.d/monetdb.list
echo "deb-src https://dev.monetdb.org/downloads/deb/ $(lsb_release -cs) monetdb" >> /etc/apt/sources.list.d/monetdb.list
sudo apt update
sudo apt install -y  monetdb5-sql monetdb-client
sudo systemctl enable monetdbd
sudo systemctl start monetdbd
sudo usermod -a -G monetdb $USER
sudo rm /usr/lib/x86_64-linux-gnu/monetdb5/createdb/72_fits.sql
sudo rm /usr/lib/x86_64-linux-gnu/monetdb5/fits.mal
sudo monetdbd create /var/monetdb5/dbfarm
sudo monetdbd start /var/monetdb5/dbfarm
monetdb create voc
monetdb release voc
mclient -u monetdb -d voc
