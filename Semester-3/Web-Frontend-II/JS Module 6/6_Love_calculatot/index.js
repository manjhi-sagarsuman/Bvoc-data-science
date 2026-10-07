let yourName = prompt("Enter your name");
let partnerName = prompt("Enter your partner's name");

let loveScore = Math.random() * 100;
loveScore = Math.floor(loveScore) + 1;
if (loveScore > 70) {
    alert("Your love score is " + loveScore + "%. You are a graet match!");
} else {
    alert("Your love score is " + loveScore + "%. You need to work on your relationship.");
}