
function addToCart(name, price, image_url, size) {
    let productHTML = `
    <div class="col-md-4">
      <div class="sepet-urun">
        <img class="img" src="${image_url}" alt="Ürün Görseli" />
        <div class="content">
          <div class="product-info">
            <h2 class="product-name">${name}</h2>
            <h4 class="price">${price}</h4>
          </div>
          <hr />
          <div class="actions">
            <button class="remove-btn"><i class="fa-solid fa-trash" style="color: #63E6BE;"></i></button>
            <input type="number" class="quantity-input" value="1" />
          </div>
        </div>
      </div>
    </div>
  `;
    console.log("Sepete eklenen ürün:", name, price, image_url, size);
}

// Beden butonlarına tıklandığında ürünü sepete eklemek için event listener ekleyelim
document.addEventListener('DOMContentLoaded', function () {
    let sizeButtons = document.querySelectorAll('.size-btn');

    sizeButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            let productElement = event.target.closest('.yeni-yapi');
            let name = productElement.querySelector('.product-name').textContent;
            let price = productElement.querySelector('.price').textContent;
            let image_url = productElement.querySelector('.img').getAttribute('src');
            let size = event.target.textContent;

            addToCart(name, price, image_url, size);
        });
    });
});

