<html>
<body>

<form action="index.php" method="post" enctype="multipart/form-data">
    <input type="file" name="uploadedfile">
    <input type="submit" value="Upload">
</form>

</body>
</html>

<?php
$target = "/var/www/html/uploads/";
$target = $target . basename($_FILES["uploadedfile"]["name"]);


if (move_uploaded_file($_FILES["uploadedfile"]["tmp_name"], $target)) 
{
	echo "The file ". basename( $_FILES["uploadedfile"]["name"]). " has been uploaded.";
} 
else 
{
	echo "Sorry, there was an error uploading your file.";
}
?>
