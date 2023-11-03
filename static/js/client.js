var cart = null;

function addFruitToCart(pid, qty){

}

function addToCart(pid, qty, category)
{
  if(cart == null){
    
  }
}

function getCart(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {

      if (this.readyState == 4 && this.status == 200) {
          alert(this.responseText);
      }
    };
    xhttp.open("GET", "http://127.0.0.1:8350/api/cart", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send();
  }