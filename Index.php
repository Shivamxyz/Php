
<?php

$number = $_GET['number'];
$url = "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile";

$headers = array(
    "Accept-Charset: UTF-8",
    "Content-Type: application/json; charset=UTF-8",
    "Accept-Encoding: gzip",
    "User-Agent: Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
    "Host: prod.milkbasket.com",
    "Connection: Keep-Alive",
    "Content-Length: 94"
);

$data = array(
    "retry" => true,
    "mobile" => "$number",
    "retryType" => "voice",
    "loaderMessage" => "Initializing call.."
);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

$response = curl_exec($ch);

if ($response === false) {
    echo "Error: " . curl_error($ch);
} else {
    echo "API Response: " . $response;
}

curl_close($ch);

$url1 = "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile";

$headers1 = array(
    "Accept-Charset: UTF-8",
    "Content-Type: application/json; charset=UTF-8",
    "Accept-Encoding: gzip",
    "User-Agent: Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
    "Host: prod.milkbasket.com",
    "Connection: Keep-Alive",
    "Content-Length: 48"
);

$data1 = array(
    "mobile" => "$number",
    "appHash" => "tG3K6W/hoYi"
);

$ch = curl_init($url1);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data1));

$response = curl_exec($ch);

if ($response === false) {
    echo "Error: " . curl_error($ch);
} else {
    echo "API Response: " . $response;
}

curl_close($ch);
?>
