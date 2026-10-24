console.log('Loading editor..')

window.onload = () => {
  const csrf_token = Cookies.get('csrftoken')

  document.querySelectorAll('textarea.vLargeTextField').forEach(element => {
    ClassicEditor
      .create(element, {
        toolbar: {
          items: [
            'heading',
            '|',
            'bold',
            'alignment',
            'italic',
            'horizontalLine',
            'link',
            'bulletedList',
            'numberedList',
            '|',
            'indent',
            'outdent',
            '|',
            'blockQuote',
            'insertTable',
            'imageInsert',
            'mediaEmbed',
            'undo',
            'redo'
          ]
        },
        language: 'en',
        image: {
          toolbar: [
            'imageTextAlternative',
            'imageStyle:full',
            'imageStyle:side'
          ]
        },
        table: {
          contentToolbar: [
            'tableColumn',
            'tableRow',
            'mergeTableCells'
          ]
        },
        simpleUpload: {
          uploadUrl: '/articles/image/upload/',
          headers: {
            'X-CSRFToken': csrf_token
          }
        }
      })
      .then(editor => {console.log('Editor loaded')})
      .catch(error => {console.log('Error occurred during editor loading', error)})
  })
}
