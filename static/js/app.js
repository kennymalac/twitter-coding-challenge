var API_ROOT = window.location + 'api/';
var template_cache = {};

function get_form_data(formSelector) {
    return $(formSelector).serializeArray().reduce(function (obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});
}

function on_load() {
    templates = {
        list_tweets: $('#list-tweets-template').html(),
        tweet_reply_modal: $('#tweet-reply-modal-template').html()
    };
    // Pre-cache mustache templates
    Mustache.parse(templates.list_tweets);
    Mustache.parse(templates.tweet_reply_modal);

    // Setup event handlers
    $('.timeline-form input[type=submit]').on('click', function(e) {
        e.preventDefault();

        var form_data = get_form_data(".form");

        var data = {};

        // Input validation
        var valid_user = new RegExp("[A-Za-z0-9_]+");
        if (valid_user.test(form_data.userid)) {
            // The user could be a valid user.
            // Run the API call
            get_twitter_timeline(form_data.userid);
        } else {
            show_status_message("error", "Please enter a valid twitter username.");
        }
    });
}
$(document).ready(on_load);

function show_status_message(type, msg) {
    var $message = $('p.message');
    $message.removeClass('bg-' + $message.data('type'));

    if (type == "error") {
        $message.data('type', 'danger');
        $message.addClass('bg-danger');
    } else if (type == "success") {
        $message.data('type', 'success');
        $message.addClass('bg-success');
    }

    $message.text(msg);
}

function render_tweets(data) {
    data.momentizeUnix = function() {
        return function(text, render) {
            return moment.unix(render(text)).fromNow();
        };
    };
    $('.tweet-list').html(
        Mustache.render(templates.list_tweets, data));

    // Bind the tweet's data in the reply modal
    $('.reply .btn').click(function(e) {
        var $elem = $(e.currentTarget);
        var $modal = $('.reply-modal');
        var $tweet = $elem.parents('.tweet');
        var data = {
            tweet: {
                id: $tweet.data('id'),
                text: $tweet.find('.text').text()
            },
            'user': {
                id: $tweet.find('.user-legend').data('id')
           } 
        };

        $modal.html(
            Mustache.render(templates.tweet_reply_modal, data));
        $modal.modal();
    });
}

function get_twitter_timeline(twitter_userid) {
    fetch(API_ROOT + 'twitter/timeline/' + twitter_userid)
        .then(function(response) {
            if (response.status >= 200 && response.status < 300) {
                return response.json();
            } else {
                var error = new Error(response.statusText);
                error.response = response;
                throw error;
            }
        }).then(function(data) {
            // Handle tweets JSON
            console.log(data);
            show_status_message("success", "Loaded public timeline");
            render_tweets({
                tweets: data
            });
        }).catch(function(err) {
            console.log(err);
            if (err.response.status == 500) {
                show_status_message("error", "A server error has occurred.");
            }
            else if (err.response.status == 400) {
                show_status_message("error", err.response.error);
            }
            else {
                show_status_message("error", "An unknown error has occurred.");
            }
        });
}

