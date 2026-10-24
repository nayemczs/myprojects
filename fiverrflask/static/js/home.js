const audio_players = document.querySelectorAll(".custom_audio");

audio_players.forEach(audio_player => {
    audio_player.addEventListener("pause", () => {
        const data = {
            'player_id': audio_player.getAttribute('player_id'),
            'current_position': audio_player.currentTime.toFixed(2)
        };

        save_json(
            data,
            (audio_player.currentTime.toFixed(2) === audio_player.duration.toFixed(2))
        )

        console.log(`Audio paused for player ${audio_player.getAttribute('player_id')}`)
    })

    audio_player.addEventListener('play', () => {
        Array.from(audio_players).filter(player =>
            player.getAttribute('player_id') !== audio_player.getAttribute('player_id')
        ).forEach(player => {
            if (!player.paused)
                player.pause()
        })
    })
})

document.querySelector('body').addEventListener("beforeunload", (event) => {
    event.preventDefault()
    const audio_player = Array.from(audio_players).find(player => !player.paused)
    const data = {
        'player_id': audio_player.getAttribute('player_id'),
        'current_position': audio_player.currentTime.toFixed(2)
    };

    save_json(data)
    return ''
})

function save_json(data, mark_listened=false) {
    const xhr = new XMLHttpRequest()
    if (mark_listened)
        xhr.open('POST', mark_listened_url, true)
    else
        xhr.open('POST', save_position_url, true)
    xhr.setRequestHeader('X-CSRFToken', csrf_token)

    const form_data = new FormData()
    form_data.set('data', JSON.stringify(data))

    xhr.onload = function () {
      if (this.status === 200) {
        console.log(this.responseText)
      } else
        console.log(this.responseText)
    }
    xhr.send(form_data)

    console.log('Properties saved:', data)
}