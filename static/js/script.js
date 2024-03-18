// favorites.js

// Favori ekleme işlevi
function addToFavorites(productId) {
  // Favori ekleme işlemi
  // Burada ürün ID'sine göre favori ekleme işlemini gerçekleştiriyoruz
  // Örneğin, favori eklendiğinde bir mesajı ekrana yazdırabiliriz
  var message = "Ürün favorilere eklendi: " + productId;
  document.getElementById("statusMessage").innerText = message;
}
