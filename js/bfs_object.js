// Объект на вход
const object = {
    a: {
        d: {
            h: 4
        },
        e: 2
    },
    b: 1,
    c: {
        f: {
            g: 3,
            k: {}
        }
    }
};

const addLevels = (obj) => {

    const copyObj = JSON.parse(JSON.stringify(obj));
    let st = [{obj: copyObj, level: 0}];

    while(st.length > 0)
    {
        const { obj, level } = st.pop();

        for (let key in obj) {
            if (typeof(obj[key] === 'object' && obj[key] !== null )){
                obj[key].level = level+1;
                st.push({obj: obj[key], level:level + 1});
            }
        }
    }

    copyObj.level = 0;

    return copyObj;


}

console.log(addLevels(object))
