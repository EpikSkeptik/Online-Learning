import PropTypes from 'prop-types'
import Button from './Button'

const Header = (props) => {
    const onClick = (e) => {
        console.log(e)
    }
    return (
        <header className='header'>
            <h1>{props.title}</h1>
            <Button onClick={onClick} color='steelblue' text='Add'/>
        </header>
    )
}

Header.defaultProps = {
    title: 'Task Tracker',
}

Header.propTypes = {
    title: PropTypes.string.isRequired,
}

export default Header
