// JavaScript dosyası (örneğin, script.js)

function addToFavorites(urunId) {
    // Favori ekleme işlemleri burada yapılacak
    // Örneğin: Favori eklenen ürünün id'sini bir form aracılığıyla sunucuya göndermek
    let form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/favori-ekle/'); // Favori ekleme URL'si

    let csrfToken = document.createElement('input');
    csrfToken.setAttribute('type', 'hidden');
    csrfToken.setAttribute('name', 'csrfmiddlewaretoken');
    csrfToken.setAttribute('value', '{{ csrf_token }}'); // Django CSRF token'ı

    let urunIdInput = document.createElement('input');
    urunIdInput.setAttribute('type', 'hidden');
    urunIdInput.setAttribute('name', 'urun_id');
    urunIdInput.setAttribute('value', urunId);

    form.appendChild(csrfToken);
    form.appendChild(urunIdInput);

    document.body.appendChild(form);
    form.submit();
}

function deleteFavorite(favoriteId) {
    // AJAX kullanarak favori silme isteği gönder
    fetch('/favori-sil/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}' // Django CSRF token'ı
        },
        body: JSON.stringify({ favorite_id: favoriteId })
    })
        .then(response => {
            if (response.ok) {
                // Favori başarıyla silindiğinde yapılacak işlemler
                // Örneğin, favori listesini yeniden yükleme
                location.reload();
            } else {
                throw new Error('Favori silinemedi.');
            }
        })
        .catch(error => {
            console.error('Hata:', error);
        });
}
