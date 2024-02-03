class Hero{
    constructor(nome, idade, tipo){
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
    }

    atacar(){
        let tipoAtaque

        if(this.tipo === 'mago'){
            tipoAtaque = 'magia'
        }else if(this.tipo === 'guerreiro'){
            tipoAtaque = 'espada'
        }else if(this.tipo === 'monge'){
            tipoAtaque = 'artes marciais'
        }else if(this.tipo === 'ninja'){
            tipoAtaque = 'shiriken'
        }
        console.log(`O ${this.nome} atacou usando ${tipoAtaque}`)
    }
}

hero7 = new Hero('Cristiano Ronaldo',39,'guerreiro')
hero10 = new Hero('Messi', 37, 'ninja')
hero7.atacar()
hero10.atacar()

