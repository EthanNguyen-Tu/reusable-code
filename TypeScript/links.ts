export function getYoutubeThumbnail(videoId: string) {
    return `https://i1.ytimg.com/vi/${videoId}/sddefault.jpg`;
}

export function getNoCookieYoutubeLink(videoId: string, si: string) {
    return `https://www.youtube-nocookie.com/embed/${videoId}?si=${si}&autoplay=1`;
}
