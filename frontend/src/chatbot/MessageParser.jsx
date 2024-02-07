import React from 'react';

const actions = {
    greet: () => console.log('Hello!'),
    farewell: () => console.log('Goodbye!'),
};

const MessageParser = ({ children }) => {
    const parse = (message) => {
        if (message.includes('hello')) {
            actions.greet();
        } else if (message.includes('bye')) {
            actions.farewell();
        }
    };

    return (
        <div>
            {React.Children.map(children, (child) => {
                return React.cloneElement(child, {
                    parse: parse,
                    actions: actions,
                });
            })}
        </div>
    );
};

export default MessageParser;