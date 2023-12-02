myStorage = window.localStorage;

var fileName = location.pathname.split("/").slice(-1)[0];
// alert();
console.log(fileName);

if (fileName == 'index.html') {

const input = document.getElementById('employeeName');

input.addEventListener('focus', function() {
    if (input.value === 'например, Иванов') {
        input.value = '';
    }
});

input.addEventListener('blur', function() {
    if (input.value === '') {
        input.value = 'например, Иванов';
    }
});


const numberInput = document.getElementById('numberInput');
const submitButton = document.getElementById('submitButton');
const errorMessage = document.getElementById('errorMessage');
const closeButton = document.getElementById('closeButton');

submitButton.addEventListener('click', function() {
    const userInput = numberInput.value.trim();

    if (isNaN(userInput)) {
        // Если введенная последовательность не является числом
        errorMessage.style.display = 'block';
    } else {
        // Если введенная последовательность является числом
        errorMessage.style.display = 'none';
        // Здесь можно выполнить необходимые действия с числом, например:
        console.log('Введенное число:', parseInt(userInput, 10));
    }
});

closeButton.addEventListener('click', function() {
    errorMessage.style.display = 'none';
});


const delButton = document.getElementById('deleteButton');

// confirm("Точно удалить?");

delButton.addEventListener('click', function() {
    const result = confirm("Точно удалить?");

    if (result == true) {
        console.log('true');

        var a = document.getElementsByClassName("yourClassName");
        for(var key in a) {
            if (a[key].checked == true) {
                a[key].parentNode.parentNode.parentNode.removeChild(a[key].parentNode.parentNode);
            }
        }
        // console.log(a);

    } else {
        console.log('false');
    }
});




const searchName = document.getElementById('searchName');

searchName.addEventListener('click', function() {
    console.log('test');

    var t;

    if (input.value === 'например, Иванов') {
        t = '';
    } else {
        t = input.value;
    }

    
    localStorage.setItem("name", t);
    open('newDoc.html');


});

}


if (fileName == 'newDoc.html') {
    const newInput = document.getElementById('newInput');
    newInput.value = localStorage.getItem('name');

}
