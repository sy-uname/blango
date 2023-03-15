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
    dataLoaded: true,
    data: {
      results: [
        {
          id: 17,
          tags: [
            'django', 'react'
          ],
          'hero_image': {
            'thumbnail': '/media/__sized__/hero_images/photo_1_2023-03-06_16-37-31-thumbnail-100x100-70.jpg',
            'full_size': '/media/hero_images/photo_1_2023-03-06_16-37-31.jpg'
          },
          title: 'Test Post',
          slug: 'test-post',
          summary: 'A test post, created for Django/React.'
        }
      ]
    }
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
}

ReactDOM.render(
  React.createElement(PostTable),
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
