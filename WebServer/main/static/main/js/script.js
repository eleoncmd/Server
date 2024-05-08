document.querySelectorAll('.catalog__wrap input').forEach(item => {

    item.addEventListener('mousemove', function() {

        this.closest('.catalog__wrap').querySelector('.catalog__value').innerHTML = this.value;
    })

});