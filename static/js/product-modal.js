// Получаем кнопку и модальное окно
var buttonsClose = document.querySelectorAll(".close-btn");
var buttonsDetails = document.querySelectorAll(".details-btn");
var modals = document.querySelectorAll(".modal");

// Добавляем обработчик события к каждой кнопке "Подробнее"
buttonsDetails.forEach(function(btn, index){
    btn.onclick = function(){
        modals[index].classList.toggle("show"); // Отображаем модальное окно
    };
});

// Добавляем обработчик события к каждой кнопке "Закрыть"
buttonsClose.forEach(function(btn, index){
    btn.onclick = function(){
        if (modals[index].classList.contains('modal')) { // Проверяем клик вне окна
            modals[index].classList.remove("show"); // Скрываем модальное окно
        }
    };
});