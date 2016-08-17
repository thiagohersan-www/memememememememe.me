window.onload = function() {
  var FOF_TOKEN = "?ref=404";
  var mUrl = window.location.href;

  if(mUrl.endsWith(FOF_TOKEN)) {
    mUrl = mUrl.replace(FOF_TOKEN, "");
    var urlArr = mUrl.split("/");
    var pageName = urlArr[urlArr.length-1].replace(/[0-9]+$/, "");

    var outputMessage = "Sorry! I really can't find <b>";
    outputMessage += pageName;
    outputMessage += "</b>  -- Trying on google .";

    var contentElement = document.getElementById("post").getElementsByTagName("content")[0]
    contentElement.innerHTML = outputMessage;

    setTimeout(function() {
      window.location.href = "https://www.google.com.br/search?q=site%3Ahttp://www.memememememememe.me/+"+pageName;
    }, 5555);

    setInterval(function() {
      contentElement.innerHTML += ".";
    }, 555);
  }
  else {
    var newUrl = mUrl.replace(/-?[0-9]+(\/)?$/, "/");
    window.location.href = newUrl+""+FOF_TOKEN;
  }
};
