import "./UploadBox.css"

function UploadBox() {

  return (
    <div className="uploadBox">

      <div className="uploadIcon">⬆</div>
      <p>Drop audio file or click to upload</p>
      <span>.wav .mp3 .m4a .ogg</span>
      <input type="file" />

    </div>
  )
}

export default UploadBox