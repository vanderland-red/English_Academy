// این برای زمانی هستش که کاربر اگر فرم رو خالی گذاشت براش پیام هشدار فارسی بنویسه

document.addEventListener("DOMContentLoaded", function () {

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("invalid", function (event) {

            const input = event.target;

            if (input.validity.valueMissing) {
                input.setCustomValidity(
                    "لطفاً این کادر را تکمیل کنید."
                );
            }

        }, true);


        form.addEventListener("input", function (event) {

            const input = event.target;

            input.setCustomValidity("");

        });

    });

});