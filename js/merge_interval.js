

const array3 = [[11, 12], [2, 3], [5, 7], [1, 4], [8, 10], [6, 8]]
const array1 = [[1, 3], [2, 6], [8, 10], [15, 18]]; // [[1, 6], [8, 10], [15, 18]]
const array2 = [[1, 4], [4, 5]];


console.log(array1.sort((a,b)=>{
    if (a[0] > b[0])
    {
        return 1;
    }
    return -1;
}));

function merge(intervals)
{
    const union     = (r1, r2) => [Math.min(r1[0], r2[0]), Math.max(r1[1], r2[1])];

    let res = [];
    res.push(intervals[0])

    let j = 0;

    for (let i = 1; i < intervals.length; i++)
    {
        let l2 = intervals[i][0];
        let r2 = intervals[i][1];

        if (l2 > res[j][0] && r2 < res[j][1])
        {
            continue;
        } else if (l2 >= res[j][0] && l2 <= res[j][1] && r2 >= res[j][1])
        {
            res[j][1] = r2;
        } else if (res[j][1] < l2)
        {
            j++;
            res.push([l2,r2]);
        }
    }

    console.log(res);
}
merge(array2);
merge(array1);

