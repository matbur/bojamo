/**
 * Created by matbur on 31.12.16.
 */

class Users extends React.Component {
    constructor() {
        super();

        this.state = {
            users: [],
            counter: 0,
        }
    }

    componentWillMount() {
        this._getUsers();
    }

    render() {
        const users = this.state.users;
        return (<div>
            <p>{this.state.counter}</p>
            {users.map((user) => <p>{user['fields']['email']}</p>)}
        </div>)
    }

    componentDidMount() {
        this._timer = setInterval(() => this._getUsers(), 5000)
    }

    componentWillUnmount() {
        clearInterval(this._timer)
    }

    _getUsers() {
        $.ajax({
            method: 'GET',
            url: '/api?last_name=bur',
            success: (users) => {
                this.setState({users})
            }
        })
        let counter = this.state.counter + 1
        this.setState({counter})
    }
}

class App extends React.Component {
    constructor() {
        super()
        this.state = {
            loggedIn: false
        }
    }

    render() {
        let login;
        if (!this.state.loggedIn) {
            login = <LoginUser/>
        }
        return (<div>
            {login}
        </div>)
    }
}

class LoginUser extends React.Component {
    constructor(props) {
        super(props);
        this._handleSubmit = this._handleSubmit.bind(this);
        this.state = {
            username: '',
            password: ''
        }
    }

    _handleSubmit(event) {
        event.preventDefault();
        console.log(this._username.value + ':' + this._password.value);

        $.ajax('/api/login', {
            success: (response) => {
                if (response.status) {
                    console.log('ok')
                } else {
                    console.log('error')
                }
            },
            data: {
                username: this._username.value,
                password: this._password.value
            }
        })
    }

    render() {
        return (
            <form onSubmit={this._handleSubmit}>
                <p>
                    <label>
                        Username:
                        <input type="text" ref={(input) => this._username = input}/>
                    </label>
                </p>
                <p>
                    <label>
                        Password:
                        <input type="password" ref={(input) => this._password = input}/>
                    </label>
                </p>
                <input type="submit" value="Submit"/>
            </form>
        );
    }
}

ReactDOM.render(
    <App/>, document.getElementById('app')
);
