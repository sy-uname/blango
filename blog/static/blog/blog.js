['/', '/api/v1/posts/', '/abadurl/'].forEach(url => {
  fetch(
    url
  ).then(response => {
    if (response.status !== 200) {
      throw new Error('Invalid status from server: ' + response.statusText)
    }
    return response.json()
  }).then(data => {
    // do something with data, for example
    console.log(data)
  }).catch(e => {
    console.error(e)
  })
})

class ClickButton extends React.Component {
  state = {
    wasClicked: false
  }

  handleClick () {
    this.setState(
      {wasClicked: true}
    )
  }

  render () {
    let buttonText

    if(this.state.wasClicked)
      buttonText = 'Clicked!'
    else
      buttonText = 'Click Me'

    return <button className='btn btn-primary mt-2' onClick={ () => { this.handleClick() } } >{buttonText}</button>
   }
}

const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(ClickButton),
  document.getElementById('react_root_second')
)

class PostRow extends React.Component {
  render () {
    const post = this.props.post

    let thumbnail

    if (post.hero_image.thumbnail) {
      thumbnail = <img src={post.hero_image.thumbnail}/>
    } else {
      thumbnail = '-'
    }

    return <tr><td className="text-light">{post.title}</td><td>{thumbnail}</td><td className="text-light">{post.tags.join(', ')}</td><td className="text-light">{post.slug}</td><td className="text-light">{post.summary}</td><td className="text-light"><a href={'/post/' + post.id }>View</a></td></tr>
  }
}

class PostTable extends React.Component {
  state = {
    dataLoaded: false,
    data: null
  }

  render () {
    let rows
    if (this.state.dataLoaded) {
      if (this.state.data.results.length) {
        rows = this.state.data.results.map(post => <PostRow post={post} key={post.id}/>)
      } else {
        rows = <tr><td colSpan="6">No results found.</td></tr>
      }
    } else {
      rows = <tr><td colSpan="6">Loading&hellip;</td></tr>
    }

    return <table className="table table-striped table-bordered mt-2 text-light"><thead><tr><th>Title</th><th>Image</th><th>Tags</th><th>Slug</th><th>Summary</th><th>Link</th></tr></thead><tbody>{rows}</tbody></table>
  }

  componentDidMount () {
    fetch(this.props.url).then(response => {
      if (response.status !== 200) {
        throw new Error('Invalid status from server: ' + response.statusText)
      }

      return response.json()
    }).then(data => {
      this.setState({
        dataLoaded: true,
        data: data
      })
    }).catch(e => {
      console.error(e)
      this.setState({
        dataLoaded: true,
        data: {
          results: []
        }
      })
    })
  }
}

ReactDOM.render(
  React.createElement(PostTable,{url: postListUrl}),
  domContainer
)


function resolvedCallback(data) {
  console.log('Resolved with data ' +  data)
}

function rejectedCallback(message) {
  console.log('Rejected with message ' + message)
}

const lazyAdd = function (a, b) {
  const doAdd = (resolve, reject) => {
    if (typeof a !== "number" || typeof b !== "number") {
      reject("a and b must both be numbers")
    } else {
      const sum = a + b
      resolve(sum)
    }
  }

  return new Promise(doAdd)
}

const p = lazyAdd(3, 4)
p.then(resolvedCallback, rejectedCallback)

lazyAdd("nan", "alsonan").then(resolvedCallback, rejectedCallback)
