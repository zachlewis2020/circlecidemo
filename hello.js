
console.log("hello works")

var params = {Bucket: 'bucket', Key: 'key', Body: stream};
s3.upload(params, function(err, data) {
    console.log(err, data);
});
