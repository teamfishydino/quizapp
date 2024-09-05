# Data Models

## Quiz

```js
{
    _id: ObjectId,
    name: String,
    creator: String,
    createdAt: Date,
    tags: String[],
    questions: [
        {
            question: String,
            answer: Boolean
        }
    ]
}
```

**Constraints**

`name`
- required
- unique
- MaxLength: [30](https://stackoverflow.com/a/17087528)

`creator`
- required
- default value: "Anonymous"

`createdAt`
- required
- should be >= current date

`tags`
- optional
- max length: 30
- no duplicate array items (set)

`questions`
- required
- no duplicate questions
- `question` field max length: 140

