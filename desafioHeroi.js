let heroName = 'Meliodas'
let heroExp = 1001
let heroElo


//Foi realizada uma alteração no que é solicitado no enunciado relacionada a primeira condicional, visto que o valor deveria ser < 1000
// o que criaria um possivél gap entre os valores, sendo assim, o primeiro if é inclusivo, ou seja, <= 1000



if(heroExp <= 1000){
    heroElo = 'Ferro'
}else if(heroExp<=2000){
    heroElo = 'Bronze'
}else if(heroExp <= 5000){
    heroElo = 'Prata'
}else if(heroExp <= 7000){
    heroElo = 'Ouro'
}else if(heroExp <= 8000){
    heroElo = 'Platina'
}else if(heroExp <= 9000){
    heroElo = 'Ascendente'
}else if(heroExp <= 10000){
    heroElo = 'Imortal'
}else{
    heroElo = 'Radiante'
}

console.log("O Herói de nome " + heroName+ " está no nível de "+heroElo)

