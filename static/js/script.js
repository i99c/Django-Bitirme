// script.js
document.addEventListener('DOMContentLoaded', function () {
    let favButtons = document.querySelectorAll('.fav-btn');
    let cartButtons = document.querySelectorAll('.cart-btn');
    let deleteButtons = document.querySelectorAll('.delete-btn');

    // Favori ekleme işlevi
    favButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            console.log('Favorilere eklendi: ' + this.parentElement.parentElement.querySelector('.product-name').innerText);
            // Favorilere ekleme işlemleri buraya gelecek
        });
    });

    // Sepete ekleme işlevi
    cartButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            console.log('Sepete eklendi: ' + this.parentElement.parentElement.querySelector('.product-name').innerText);
            // Sepete ekleme işlemleri buraya gelecek
        });
    });

    // Ürünü silme işlevi
    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            console.log('Ürün silindi: ' + this.parentElement.parentElement.querySelector('.product-name').innerText);
            // Ürünü silme işlemleri buraya gelecek
        });
    });
});
