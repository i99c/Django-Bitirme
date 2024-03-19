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
    // Favori silme işlemleri burada yapılacak
    // Örneğin: Favori silinecek favori id'sini bir form aracılığıyla sunucuya göndermek
    let form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/favori-sil/'); // Favori silme URL'si

    let csrfToken = document.createElement('input');
    csrfToken.setAttribute('type', 'hidden');
    csrfToken.setAttribute('name', 'csrfmiddlewaretoken');
    csrfToken.setAttribute('value', '{{ csrf_token }}'); // Django CSRF token'ı

    let favoriteIdInput = document.createElement('input');
    favoriteIdInput.setAttribute('type', 'hidden');
    favoriteIdInput.setAttribute('name', 'favorite_id');
    favoriteIdInput.setAttribute('value', favoriteId);

    form.appendChild(csrfToken);
    form.appendChild(favoriteIdInput);

    document.body.appendChild(form);
    form.submit();
}
