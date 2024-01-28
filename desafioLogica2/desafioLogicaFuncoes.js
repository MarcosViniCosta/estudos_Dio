let wonBattles = 80
let defeats = 33
let heroRanking


function battlesCalc(wonBattles,defeats){
    return wonBattles - defeats
}

function heroElo(battleStatistcs){
    
    if(battleStatistcs <= 10){
        return "Ferro"
    }else if(battleStatistcs <= 20){
        return "Bronze"
    }else if(battleStatistcs <= 50){
        return "Prata"
    }else if(battleStatistcs <= 80){
        return "Ouro"
    }else if(battleStatistcs <= 90){
        return "Diamante"
    }else if(battleStatistcs <= 100){
        return "Lendário"
    }else{
        return "Imortal"
    }

}

let battleStatistcs = battlesCalc(wonBattles,defeats)
heroRanking = heroElo(battleStatistcs)

console.log(`O Herói tem o saldo de ${battleStatistcs} vitórias, e está no nível ${heroRanking}`)