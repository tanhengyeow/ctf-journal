e = "8e15ad6e5f26fe0585707dc97ce967c6ffaac0cacd2037c4c6c63a503ceea1e6U2FsdGVkX1+yNXzSLU+2HUI7GTRvpl9BdTD1OPX5iMZgHlYay52uv5t/UEHRkeKLJyFjgCoV2nxfL17HPAz8e3bQy0tm0VtorCHXuW/IauNEynVQygPQzaob/1eRihkfYf1XW59GQscAf9uDz93Dub7qiIn5WMIH6hzkM1yDbDBXb6U4GdZQWYsqoFStfyBGaQ04DnnrN3qU/kSs3ciVGmWyW3vuPSHw26VwmINr1jF16DKGK8YWBExVgu9zhiNBaxyQIuWs2SX2BVHokVBOKg==";

r = e.substring(0,64);
c = e.substring(64);
a = "";

function brute(a) {
    var CryptoJS = require("crypto-js");
    if (CryptoJS.HmacSHA256(c, CryptoJS.SHA256(a)).toString() === r) {
        var n = CryptoJS.AES.decrypt(c, a).toString(CryptoJS.enc.Utf8);
        console.log(n);
        process.exit();
    }
}

// Thanks to https://stackoverflow.com/questions/6156501/read-a-file-one-line-at-a-time-in-node-js
var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('rockyou.txt')
});

lineReader.on('line', function (line) {
    //console.log(line);
    brute(line);
});
