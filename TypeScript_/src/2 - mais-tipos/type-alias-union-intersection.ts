type User = {
    name: string;
    lastName: string;
    birthday: string;
    age?: number;  // o '?' mostra que é opcional
}

const gabriel: User = {
    name: 'Lucas',
    lastName: 'Oliveira',
    birthday: '09/10/2000'
}


// union typescript
// |

type LogLevel = 'info' | 'error' | 'debug';

function logMessage(message: string, level: LogLevel){
    console.log(`[${level}] - ${message}`)
}

logMessage('Uma mensagem info', 'info')
logMessage('Uma mensagem info', 'error')
logMessage('Uma mensagem info', 'debug')

// intersection types 
// &

type About = {
    bio: string,
    interests: string[]
}

type Profile = User & About;

const userWithProfile: Profile = {
    name:'Lucas',
    lastName: 'Oliveira',
    birthday: '09/10/2000',
    bio: 'Olá, meu nome é Lucas',
    interests: ['gatos', 'jogos', 'livros']
}