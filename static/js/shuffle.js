
function shuffleList(classSelector) {
    let ul = document.querySelector(classSelector);
    for (var i = ul.children.length; i >= 0; i--) {
        ul.appendChild(ul.children[Math.random() * i | 0]);
    }
}