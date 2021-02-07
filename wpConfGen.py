####Note: Filepath and database name will be the same will 
####be the same. 
import requests
import argparse
parser = argparse.ArgumentParser()
url = "https://api.wordpress.org/secret-key/1.1/salt/"
res = requests.get(url)
saltApi = res.text
parser.add_argument("-f", "--filepath", type=str, help="Filepath, for now it is the same as dbname NOT NEEDED")
parser.add_argument("-b", "--dbname", type=str, help="the name of the database")
args = parser.parse_args()
dbName = str(args.dbname)
filePath = dbName
permitted = True
if dbName == "None":
  print("CAN NOT CONTINUE, there is no value")
  permitted = False

if permitted:
  filepath = dbName
  confText = "<?php\r\ndefine( \'DB_NAME\', \'" + dbName + "\' );\r\ndefine( \'DB_USER\', \'masteruser\' );\r\ndefine( \'DB_PASSWORD\', \'Kavip_2004\' );\r\ndefine( \'DB_HOST\', \'localhost\' );\r\ndefine( \'DB_CHARSET\', \'utf8\' );\r\ndefine( \'DB_COLLATE\', \'\' );\r\ndefine(\'FS_METHOD\', \'direct\');\r\n" +saltApi + "\r\n$table_prefix = \'wp_\';\r\ndefine( \'WP_DEBUG\', false );\r\nif ( ! defined( \'ABSPATH\' ) ) {\r\n        define( \'ABSPATH\', __DIR__ . \'/\' );\r\n}\r\n\r\nrequire_once ABSPATH . \'wp-settings.php\';"

  file1 = open("/var/www/" + filePath + "/wp-config.php", "a+")
  file1. write(confText)
  file1.close()
